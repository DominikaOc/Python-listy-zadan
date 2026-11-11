import matplotlib.pyplot as plt
import string

# zliczamy slowa w podanym pliku - funkcja z wykładu
def count_words_in_file(input_file):
    word_count = {}
    with open(input_file, encoding='utf8') as f:
        for line in f:
            words = line.split()
            for word in words: # (1)
                word = word.strip(string.punctuation).casefold() # (2, 3)
                if word == '':
                    continue
                word_count[word] = word_count.get(word, 0) + 1  # (4)
    return word_count



def draw_words_histogram_full(input_file):
    word_count = count_words_in_file(input_file)
    lst = [len(word) for word, ile in word_count.items() for _ in range(ile)]
    # kubelki postaci [n, n+1) tak, aby kazda dlugosc miala swoj kubelek
    plt.hist(lst, bins=range(0, max(lst)+2))
    plt.title(f'Ilość różnych słów o danej długości w {input_file}')
    plt.show()

#po angielsku: '20000en.txt' , 'license.txt' , 'southpole.txt' , 'prideandprejudice.txt'
# grecki: 'physica.txt' , 'politeia.txt' ,
# francuski: '20000.txt' ,
draw_words_histogram_full('politeia.txt')