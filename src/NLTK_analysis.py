from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
import pandas as pd

class descriptions():
    def __init__(self, df, descrip_col_name):
        self.df = df
        self.descrip_col_name = descrip_col_name
        self.stopWords, self.tokenizer_remove_punc, self.lemmatizer = self.init_cleaning_classes()
        self.descriptions = self.get_list_of_descriptions(self.df, self.descrip_col_name)
        self.cleaned_descriptions = self.clean_descriptions()
        self.terms, self.frequencies = self.get_term_and_freq_lists()

    def init_cleaning_classes(self):
        """
        Initiates cleaning classes from NLTK

        :params:

        None

        :returns:

        stopWords: Set of stopwords in English

        tokenizer_remove_punc: Tokenizer object to remove punctuation from text

        lemmatizer: Lemmatizer object to reduce words to stems
        """
        self.stopWords = set(stopwords.words('english'))
        self.tokenizer_remove_punc = RegexpTokenizer(r'\w+')
        self.lemmatizer = WordNetLemmatizer()
        return self.stopWords, self.tokenizer_remove_punc, self.lemmatizer


    def get_list_of_descriptions(self, df, descrip_col_name):
        """
        Extracts the list of descriptions from a pandas dataframe

        :params: 

        df: Pandas dataframe that contains descriptions

        descrip_col_name: Name of column that contains descriptions

        :returns:

        raw_description: List of descriptions
        """
        self.raw_description = df[descrip_col_name].values
        return self.raw_description


    def clean_descriptions(self):
        no_punct_descrip_list = [self.tokenizer_remove_punc.tokenize(descrip) for descrip in self.descriptions]
        word_list_no_stopwords_or_punct = []
        for descrip in no_punct_descrip_list:
            for word in descrip:
                if word.lower() not in self.stopWords:
                    word_list_no_stopwords_or_punct.append(word.lower())
        
        return [self.lemmatizer.lemmatize(word) for word in word_list_no_stopwords_or_punct]


    # def take_out_stopwords_punct(self):
    #     """
    #     Removes stopwords and punctuation from list of descriptions

    #     :params:

    #     descrip_list: List of descriptions

    #     stop_words: Array-like structure containing words to be removed from text

    #     :returns:

    #     word_list_no_stopwords_or_punct: List of words with stopwords removed, 
    #     punctuation removed, and all lowercase
    #     """
    #     no_punct_descrip_list = [self.tokenizer_remove_punc.tokenize(descrip) for descrip in self.descriptions]
    #     word_list_no_stopwords_or_punct = []
    #     for descrip in no_punct_descrip_list:
    #         for word in descrip:
    #             if word.lower() not in self.stopWords:
    #                 word_list_no_stopwords_or_punct.append(word.lower())
    #     return word_list_no_stopwords_or_punct


    # def lemmatize_word_list(word_list):
    #     """
    #     Reduces words in word list down to stems (lemmatizes)

    #     :params:

    #     word_list: List of words to be lemmatized

    #     :returns:

    #     lemmatized_word_list: List of words after being lemmatized
    #     """
    #     lemmatized_word_list = [lemmatizer.lemmatize(word) for word in word_list]
    #     return lemmatized_word_list


    def get_wordfreq_dict(self):
        """
        Creates a dictionary from a word list in which the keys 
        represent words and the values represent counts of those words

        :params:

        word_list: List of words to create frequency counts from

        :returns:

        freq_dict: Word frequency dictionary
        """
        freq_dict = dict()
        for word in self.cleaned_descriptions:
            if word in freq_dict.keys():
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
        return freq_dict


    def get_term_and_freq_lists(self):
        """
        Creates two linked lists. One list represents the list of 
        terms and the other list represents the 
        corresponding counts of occurances.
        Both lists are ordered such that the most 
        frequently appearing words are first.

        :params:

        freq_dict: Dictionary where the keys represent words 
        and the values represent their frequencies

        :returns:

        terms: List of terms ordered by frequency counts. 
        Highest counts appear first.

        freq_counts: Counts of the occurances of those words
        """
        sorted_freq_words = sorted(self.get_wordfreq_dict().items(), key=lambda item: item[1], reverse=True)
        terms = []
        freq_counts = []
        for term, freq_count in sorted_freq_words:
            terms.append(term)
            freq_counts.append(freq_count)
        return terms, freq_counts

    def search_for_term(self, term):
        term_index = self.terms.index(term.lower())
        term_freq = self.frequencies[term_index]
        print(f'{term} is ranked {term_index} with a frequency of {term_freq}')
        return term_index, term_freq


if __name__ == '__main__':
    df_all = pd.read_csv('../Datasets/df_all_linkedin.csv')
    descripts = descriptions(df_all, 'Description')
    # print(descripts.get_term_and_freq_lists())

    descripts.search_for_term('python')

    # stopWords, tokenizer_remove_punc, lemmatizer = init_cleaning_classes()
    # descrip_list = get_list_of_descriptions(df_all, 'Description')
    # word_list_no_stopwords_or_punct = take_out_stopwords_punct(descrip_list, stopWords)
    # lemmatized_cleaned_word_list = lemmatize_word_list(word_list_no_stopwords_or_punct)
    # word_freq_dict = get_wordfreq_dict(lemmatized_cleaned_word_list)
    # terms, freq_counts = get_term_and_freq_lists(word_freq_dict)

    # #Getting rank of certain terms

    # python_index = terms.index('python')
    # r_index = terms.index('r')
    # spark_index = terms.index('spark')
    # spss_index = terms.index('spss')
    # sql_index = terms.index('sql')
    # panda_index = terms.index('panda')
    # numpy_index = terms.index('numpy')
    # cloud_index = terms.index('cloud')
    # docker_index = terms.index('docker')
    # ml_index = terms.index('ml')
    # statistics_index = terms.index('statistic')
    # bi_index = terms.index('bi')

    # print(f'Python index is: {python_index}')
    # print(f'r index is: {r_index}')
    # print(f'spark index is: {spark_index}')
    # print(f'spss index is: {spss_index}')
    # print(f'sql index is: {sql_index}')
    # print(f'pandas index is: {panda_index}')
    # print(f'numpy index is: {numpy_index}')
    # print(f'cloud index is: {cloud_index}')
    # print(f'docker index is: {docker_index}')
    # print(f'ml index is: {ml_index}')
    # print(f'statistics index is: {statistics_index}')
    # print(f'bi index is: {bi_index}')

    # #Getting the actual frequency count of those terms

    # print(freq_counts[54])
    # print(freq_counts[71])
    # print(freq_counts[82])
    # print(freq_counts[107])
    # print(freq_counts[109])
    # print(freq_counts[203])
    # print(freq_counts[314])
    # print(freq_counts[340])
    # print(freq_counts[1359])
    # print(freq_counts[1396])
    # print(freq_counts[1984])
    # print(freq_counts[2270])               
