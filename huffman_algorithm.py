### Huffman Coding in python ###
#------------------------------#


sample_text = """
In this tutorial, you will learn how Huffman Coding works. Also, you will find working examples of Huffman Coding in Python.
Huffman Coding is a technique of compressing data to reduce its size without losing any of the details. It was first developed by David Huffman.
Huffman Coding is generally useful to compress the data in which there are frequently occurring characters.
For more please visit here -> https://www.programiz.com/dsa/huffman-coding.
"""

# Creating tree nodes
class Trees(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def nodes(self):
        return (self.left, self.right)

# Main function implementing huffman coding
def huffman_code(node, left=True, binString=''):

    if type(node) is str:
        return {node: binString}

    (left, right) = node.nodes()
    dict_huffman_code = dict()
    dict_huffman_code.update(huffman_code(left, True, binString + '0'))
    dict_huffman_code.update(huffman_code(right, False, binString + '1'))
    return dict_huffman_code

# Calculating frequencyuency
frequency = {}
for letter in sample_text.lower():
    if letter == " ":
        if "SP" in frequency:
            frequency["SP"] += 1
        else:
            frequency["SP"] = 1

    else:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1

frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

nodes = frequency

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = Trees(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)


dict_huffman_code = huffman_code(nodes[0][0])

encode_string = ''
for letter in sample_text.lower():
    for key in list(dict_huffman_code.keys()):
        if letter == key:
            encode_string += dict_huffman_code[key]


print("\n{} bit need to storage the sample text before encoding.\n".format(len(sample_text)*8))
print("{} bit need to storage the sample text after encoding.\n".format(len(encode_string)))
print("encode of sample text :<<{}>>\n".format(encode_string))
print(' Char | Huffman code ')
print('-------------------- ')
for (char, frequency) in frequency:
    print(' %-4r  |   %1s' % (char, dict_huffman_code[char]))