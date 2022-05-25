#Zaplavnov 5.5
from Bio import SeqIO
from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment
from Bio import Phylo
# Open and initiate the Distance Calculator using the Identity model 
from Bio.Phylo.TreeConstruction import DistanceCalculator 
calculator = DistanceCalculator('identity')

alignment = AlignIO.read('Multiple_alignment.fa',"fasta")

from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
constructor = DistanceTreeConstructor(calculator)

# Build the tree 
turtle_tree = constructor.build_tree(alignment)
turtle_tree.rooted = True
Phylo.write(turtle_tree, "turtle_tree.xml", "phyloxml")
fig = Phylo.draw(turtle_tree)
