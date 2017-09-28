from abc import ABCMeta

from bank.actions import Action


class AbstractChoice(metaclass=ABCMeta):
    _choices = None
    _display_template = None

    def add_choice(self, name, action, display_template=None):
        if not self._choices:
            self._choices = {}
        self._display_template = '%(name)s: %(action)s' if not display_template else display_template
        if name in self._choices:
            raise KeyError('Action already exist')
        self._choices[str(name)] = action

    def get_choice(self, name, atm):
        self._choices.get(str(name)).handle_action(atm)

    def display_choices(self):
        if not self._choices:
            raise ValueError('Choices are not specified')
        print('\n'.join([self._display_template
                         % {'name': name, 'action': str(action)} for name, action in self._choices.items()]))


class Choice(Action, AbstractChoice):
    """Select any option"""

    def get_name(self):
        return input('Select action> ')

    def handle_action(self, atm):
        print(self)
        self.display_choices()
        return self.get_choice(self.get_name(), atm)
