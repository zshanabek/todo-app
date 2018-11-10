export class Todo {
    constructor(
      public title: string,
      public description: string,
      public completed: boolean,
      public due_date: Date,
      public _id?: number,
      public updatedAt?: Date,
      public createdAt?: Date,
    ) { }
}