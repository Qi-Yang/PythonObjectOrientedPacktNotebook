__author__ = 'mfleming'

import datetime
# Store the next available id for all new notes
last_id = 0

class Note:
    def __init__(self, memo, tags=''):
        '''
        Initialize a note with memo and optional space separated
        tags
        :param memo:
        :param tags:
        :return:
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''
        Determine if this note matches the filter text.
        Return true if it matches, false otherwise
        :param filter:
        :return:
        '''
        return filter in self.memo or filter in self.tags

class Notebook:
    '''
    Represent a collection of notes that can me tagged, modified
    and searched

    '''

    def __init__(self):
        self.notes = []
        #List of notes


    def new_note(self, memo, tags=''):
        '''
        Create a new neote and add it to the list
        :param memo:
        :param tags:
        :return:
        '''
        self.notes.append(Note(memo,tags))

    def modify_memo(self, note_id, memo):
        '''
        Find the note with the given id and change its
        memo to the given value
        :param note_id:
        :param memo:
        :return:
        '''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False


    def modify_tags(self, note_id, tags):
        '''
        Find the note with the given ide and change ites tags to the given value

        :param note_id:
        :param tags:
        :return:
        '''
        for note in self.notes:
            if note.id == note.id:
                note.tags = tags
                break

    def search(self, filter):
        '''
        Find all notes that match the given filter string
        :param filter:
        :return:
        '''
        return [note for note in self.notes if note.match(filter)]

    def _find_note(self, note_id):
        '''
        Locate the note with the given id
        :param note_id:
        :return:
        '''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None


