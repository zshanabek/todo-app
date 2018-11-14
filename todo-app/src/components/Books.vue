<template>
   <b-container>
    <div class="row">
      <div class="col-sm-10">
        <h1>Todos</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.todo-modal>Add todo</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Description</th>
              <th scope="col">Due date</th>
              <th scope="col">Completed?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="todo in todos" :key="todo.id">
              <td>{{ todo.title }}</td>
              <td>{{ todo.description }}</td>
              <td>{{ todo.due_date }}</td>
              <td>
                <span v-if="todo.completed">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <button type="button" class="btn btn-warning btn-sm">Update</button>
                <button type="button" class="btn btn-danger btn-sm">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addTodoModal"
         id="todo-modal"
         title="Add a new todo"
         hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addTodoForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-description-group"
                      label="Description:"
                      label-for="form-description-input">
            <b-form-input id="form-description-input"
                          type="text"
                          v-model="addTodoForm.description"
                          required
                          placeholder="Enter description">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-due_date-group" 
                      label="Due date:"
                      label-for="form-due_date-input">
          <datepicker id="form-due_date-input"
                      v-model="addTodoForm.due_date"
                      required
                      placeholder="Select Date">
          </datepicker>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  </b-containter>
</template>

<script>
import axios from 'axios';
import Datepicker from 'vuejs-datepicker';
import Alert from './Alert';

export default {
  data() {
    return {
      todos: [],
      addTodoForm: {
        title: '',
        description: '',
        due_date: '',
      },
    };
  },
  components: {
    Datepicker,
    alert: Alert,
  },
  methods: {
    getTodos() {
      const path = 'http://localhost:5000/todos';
      axios.get(path)
        .then((res) => {
          this.todos = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addTodo(payload) {
      const path = 'http://localhost:5000/todos';
      axios.post(path, payload)
        .then(() => {
          this.getTodos();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getTodos();
        });
    },
    initForm() {
      this.addTodoForm.title = '';
      this.addTodoForm.description = '';
      this.addTodoForm.due_date = null;
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addTodoModal.hide();
      const payload = {
        title: this.addTodoForm.title,
        description: this.addTodoForm.description,
        due_date: this.addTodoForm.due_date, // property shorthand
      };
      this.addTodo(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addTodoModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getTodos();
  },
};
</script>
