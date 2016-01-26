import io


class DictDecomposer:
    def __init__(self, d):
        self.d = d
        self.keys = list(d.keys())
        self.values = list(d.values())

    def decompose(self):
        return self


class Converter:
    def __init__(self, delimiter=',', newline='\n'):
        self.delimiter = delimiter
        self.dict_decomposer = DictDecomposer
        self.newline = newline

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
        self.header = self.delimiter + self.delimiter.join(self.header_data)

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
                    data.append(values[h])
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
                    self.column_header_data[index],
                    self.delimiter,
                    self.delimiter.join(datum),
                    self.newline
                ])
            )
