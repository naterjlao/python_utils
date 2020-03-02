################################################################################
# File:          generateDiagrams.py
# Date created:  03/01/2020
# Author:        Nate Lao (lao.nathan@yahoo.com)
#
# Description:   Renders a diagram of SW requirements by importing CSV's and
#                a generating PDFs of the the relationships between requirements
################################################################################

import graphviz
import requirements

'''
import graphviz

dot = graphviz.Digraph(comment='The round Table')

dot.node('A', 'King Arthur')
dot.node('B','Sir Bedevere the Wise')
dot.node('L','Sir Lancelot the Brave')

dot.edges(['AB','AL'])
dot.edge('B','L',constraint='false')

print(dot.source)

dot.render('test-output/round-table.gv', view=False)
'''