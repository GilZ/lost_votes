from os import path


class DataCustomizer:
    def __init__(self):
        self.column_names = {
            'potential_voters': 'בזב',
            'legal_voters': 'כשרים'
        }
        self.threshold = 0
        self.first_party_ix = 0
        self.file_name = ''
        self.party_names = None

    def col_name(self, col):
        return self.column_names[col]

    def get_file_path(self):
        return path.join(path.dirname(__file__), '..', 'data', self.file_name)


class DataCustomizer2012(DataCustomizer):
    def __init__(self):
        super().__init__()
        self.threshold = 0.02
        self.first_party_ix = 5
        self.file_name = 'expc.csv'


class DataCustomizer2019(DataCustomizer):
    def __init__(self):
        super().__init__()
        self.threshold = 0.0325
        self.first_party_ix = 6
        self.file_name = '2019_booths.csv'
        self.party_names = {
            'ג': 'יהדות התורה',
            'דעם': 'רע"ם-בל"ד',
            'ום': 'חד"ש-תע"ל',
            'טב': 'איחוד מפלגות הימין',
            'כ': 'כולנו',
            'ל': 'ישראל ביתנו',
            'מחל': 'הליכוד',
            'מרצ': 'מרצ',
            'פה': 'כחול לבן',
            'שס': 'שס',
            'אמת': 'העבודה'
        }


class DataCustomizer2019_2(DataCustomizer):
    def __init__(self):
        super().__init__()
        self.threshold = 0.0325
        self.first_party_ix = 10
        self.file_name = '2019_2_booths.csv'
        self.party_names = {
            'ג': 'יהדות התורה',
            'ודעם': 'הרשימה המשותפת',
            'טב': 'ימינה',
            'ל': 'ישראל ביתנו',
            'מחל': 'הליכוד',
            'מרצ': 'המחנה הדמוקרטי',
            'פה': 'כחול לבן',
            'שס': 'שס',
            'אמת': 'העבודה'
        }

class DataCustomizer2020(DataCustomizer):
    def __init__(self):
        super().__init__()
        self.threshold = 0.0325
        self.first_party_ix = 10
        self.file_name = '2020_booths.csv'
        self.party_names = {
            'ג': 'יהדות התורה',
            'ודעם': 'הרשימה המשותפת',
            'טב': 'ימינה',
            'ל': 'ישראל ביתנו',
            'מחל': 'הליכוד',
            'פה': 'כחול לבן',
            'שס': 'שס',
            'אמת': 'העבודה - גשר - מרצ'
        }

