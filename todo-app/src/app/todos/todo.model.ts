export class Todo {
    constructor(
      public title: string,
      public description: string,
      public completed: boolean,
      public due_date: Date,
      public _id?: number,
      public updated_at?: Date,
      public created_at?: Date,
    ) { }
}