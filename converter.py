import io
from utils import conv_dict_to_odict


class DictDecomposer:
    def __init__(self, d):
        if type(d) == dict:
            d = self.convert(d)
        self.d = d
        self.keys = list(self.d.keys())
        self.values = list(self.d.values())

    def convert(self, d):
        return conv_dict_to_odict(d)

    def decompose(self):
        return self


class NumDictDecomposer(DictDecomposer):
    def convert(self, d):
        return conv_dict_to_odict(d, first_sort=lambda items: sorted(items, key=lambda i: int(i[0])))


class Converter:
    def __init__(
            self, delimiter=',', newline='\n',
            dict_decomposer=DictDecomposer, header_serialize=str,
            column_serialize=str, data_serialize=str):
        self.delimiter = delimiter
        self.dict_decomposer = dict_decomposer
        self.newline = newline
        self.header_serialize = header_serialize
        self.column_serialize = column_serialize
        self.data_serialize = data_serialize

    def convert(self, d, display=True, f=None, filename=None):
        self.decompose(d)
        stream = io.StringIO()

        self.create_header(self.dict_data)
        self.write_header(stream)

        self.create_column(self.dict_data)

        self.create_data(self.dict_data)
        self.write_data(stream)
        if display:
            stream.seek(0)
            print("################")
            print(stream.read())
            print("################")
        if f and filename:
            raise ValueError("Both !!")
        if f or filename:
            stream.seek(0)
            f = open(filename, 'w')
            for line in stream.readlines():
                f.write(line)

        stream.seek(0)
        return stream

    def decompose(self, d):
        decomposer = self.dict_decomposer(d)
        self.dict_data = decomposer.decompose()

    def create_header(self, dict_data, sort_call_back=sorted):
        header = set()
        for values in dict_data.values:
            header.update(values.keys())
        self.header_data = sort_call_back(header)
        self.serialized_header_data = map(self.header_serialize, self.header_data)
        self.header = self.delimiter + self.delimiter.join(self.serialized_header_data)

    def write_header(self, stream):
        stream.write(self.header + self.newline)

    def create_column(self, dict_data):
        self.column_header_data = dict_data.keys

    def create_data(self, dict_data):
        self.data_list = []
        for values in dict_data.values:
            data = []
            for h in self.header_data:
                if h in values.keys():
                    data.append(self.data_serialize(values[h]))
                else:
                    data.append('')
            self.data_list.append(data)

    def write_data(self, stream):
        for index, datum in enumerate(self.data_list):
            while 1:
                c = stream.read(1)
                if c == self.delimiter:
                    break
                if c == '':
                    break
            stream.write(
                ''.join([
                    self.column_serialize(self.column_header_data[index]),
                    self.delimiter,
                    self.delimiter.join(datum),
                    self.newline
                ])
            )
