import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import {API_URL} from '../env';
import {Todo} from './todo.model';

@Injectable()
export class TodosApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  getTodos(): Observable<Todo[]> {
    return this.http
      .get<Todo[]>(`${API_URL}/todos`)
      .catch(TodosApiService._handleError);
  }
}