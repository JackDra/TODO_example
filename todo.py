from traits.api import HasTraits, Str

class ToDo(HasTraits):

    my_string = Str('hello world')


my_todo = ToDo()

my_todo.configure_traits()