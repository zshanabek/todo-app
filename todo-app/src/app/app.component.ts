import {Component, OnInit, OnDestroy} from '@angular/core';

import {Subscription} from 'rxjs/Subscription';

import {TodosApiService} from './todos/todos-api.service';
import {Todo} from './todos/todo.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit, OnDestroy {
  title = 'todo-app';
    
  todosListSubs: Subscription;
  todosList: Todo[];

  constructor(private todosApi: TodosApiService) {
  }

  ngOnInit() {
    this.todosListSubs = this.todosApi
      .getTodos()
      .subscribe(res => {
          this.todosList = res;
        },
        console.error
      );
  }

  ngOnDestroy() {
    this.todosListSubs.unsubscribe();
  }
}
