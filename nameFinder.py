import trie
from itertools import permutations

if __name__ == "__main__":
	root = trie.TrieNode('*')
	
	#import first names
	with open ("./names/male-first-names.txt", "r") as first_names_file:
		first_names = first_names_file.readlines()
	for name in first_names:
		trie.add(root, name.lower().replace('\n', ''))

	while name != 'quit':
		name = input("Enter the letters you know with underscores for letters you don't know:\n")
		
		#get indices of unknown characters
		indice_list = [pos for pos, char in enumerate(name) if char == '_']
		
		for i in indice_list:
			name = name[:i] + 'a' + name[i + 1:]
			
		perm = permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], len(indice_list))
		
		name_set = set()
		for letters_permutation in list(perm):
			i = 0
			for indice in indice_list:
				name = name[:indice] + letters_permutation[i] + name[indice + 1:]
				if trie.find_word(root, name) == True:
					name_set.add(name)
				i = i + 1
		
		if len(name_set) == 0:
			print("No names found!")
		else:
			print(name_set)
