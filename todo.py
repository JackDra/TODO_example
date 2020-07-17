from traits.api import HasTraits, Str, List

my_to_list = ['clean car', 'create youtube video', 'feed animals']

class ToDo(HasTraits):

    todo_list = List(Str())

my_todo = ToDo(todo_list=my_to_list)

my_todo.configure_traits()