from abc import ABC, abstractmethod


class Save(ABC):
    @abstractmethod
    def save(self, *args, **kwargs):
        pass


class SaveToJSON(Save):
    def __init__(self, file_path, data_to_save):
        self.data_to_save = json.dump(data_to_save)
        self.file_path = file_path

    def save(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write(self.data_to_save)

    def show(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data_to_show = f.read(self.data_to_save)
        return json.load(data_to_show)
