<template>
   <b-container>
    <b-row>
      <b-col col sm="10">
        <h1>Todos</h1>
        <hr><br><br>
        <alert :message="message" v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.todo-modal>Add Todo</button>
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
                <button
                        type="button"
                        class="btn btn-warning btn-sm"
                        v-b-modal.todo-update-modal
                        @click="editTodo(todo)">
                    Update
                </button>
                <button
                        type="button"
                        class="btn btn-danger btn-sm"
                        @click="onDeleteTodo(todo)">
                    Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </b-col>
    </b-row>
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
                        placeholder="Enter description">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-due_date-group"
                      label="Due date:"
                      label-for="form-due_date-input">
          <datepicker id="form-due_date-input"
                      type="text"
                      v-model="addTodoForm.due_date"
                      placeholder="Select date">
          </datepicker>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editTodoModal"
         id="todo-update-modal"
         title="Update"
         hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-title-edit-group"
                      label="Title:"
                      label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-description-edit-group"
                      label="Description:"
                      label-for="form-description-edit-input">
          <b-form-input id="form-description-edit-input"
                        type="text"
                        v-model="editForm.description"
                        required
                        placeholder="Enter description">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-due_date-group"
                      label="Due date:"
                      label-for="form-due_date-input">
          <datepicker id="form-due_date-input"
                      type="text"
                      v-model="editForm.due_date"
                      placeholder="Enter date">
          </datepicker>
        </b-form-group>
        <b-form-group id="form-completed-edit-group">
          <b-form-checkbox-group v-model="editForm.completed" id="form-checks">
            <b-form-checkbox value="true">Completed?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-form>
    </b-modal>
  </b-container>
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
      editForm: {
        id: '',
        title: '',
        description: '',
        due_date: '',
        completed: [],
      },
      message: '',
      showMessage: false,
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
          this.message = 'Todo created!';
          this.showMessage = true;
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
      this.editForm.title = '';
      this.editForm.description = '';
      this.editForm.completed = [];
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
    editTodo(todo) {
      this.editForm = todo;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTodoModal.hide();
      let completed = false;
      if (this.editForm.completed[0]) completed = true;
      const payload = {
        title: this.editForm.title,
        description: this.editForm.description,
        due_date: this.editForm.due_date,
        completed,
      };
      this.updateTodo(payload, this.editForm.id);
    },
    updateTodo(payload, todoID) {
      const path = `http://localhost:5000/todos/${todoID}`;
      axios.put(path, payload)
        .then(() => {
          this.getTodos();
          this.message = 'Todo updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTodos();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTodoModal.hide();
      this.initForm();
      this.getTodos();
    },
    removeTodo(todoID) {
      const path = `http://localhost:5000/todos/${todoID}`;
      axios.delete(path)
        .then(() => {
          this.getTodos();
          this.message = 'Todo removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTodos();
        });
    },
    onDeleteTodo(todo) {
      this.removeTodo(todo.id);
    },
  },
  created() {
    this.getTodos();
  },
};
</script>
