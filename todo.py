from traits.api import HasTraits, Str, List, Button
from traitsui.api import View, Item, CheckListEditor, UItem, ListEditor, HGroup

my_to_list = ['clean car', 'create youtube video', 'feed animals']

class ToDo(HasTraits):

    add_todo_field = Str()

    add_todo = Button()

    remove_todo = Button()

    todo_list = List(Str())

    completed = List(Str())

    def _add_todo_changed(self):
        self.todo_list.append(self.add_todo_field)

    def _remove_todo_changed(self):
        self.todo_list = self.todo_list[:-1]


    my_view = View(
        Item('add_todo_field'),
        HGroup(
            UItem('add_todo'),
            UItem('remove_todo')
        ),
        UItem('completed', style='custom', editor=CheckListEditor(name='todo_list')),
        resizable=True
    )

my_todo = ToDo(todo_list=my_to_list)

my_todo.configure_traits()