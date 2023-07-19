```python
import json
from laymen_compiler.laymen_parser import parseLaymenCode

class VisualProgrammingSupport:
    def __init__(self):
        self.block_definitions = self.load_block_definitions()

    def load_block_definitions(self):
        with open('block_definitions.json', 'r') as f:
            return json.load(f)

    def generate_visual_blocks(self, laymenCode):
        parsedCode = parseLaymenCode(laymenCode)
        visualBlocks = []
        for statement in parsedCode:
            block = self.generate_block(statement)
            if block:
                visualBlocks.append(block)
        return visualBlocks

    def generate_block(self, statement):
        blockType = statement['type']
        if blockType in self.block_definitions:
            block = self.block_definitions[blockType].copy()
            for field in block['fields']:
                if field in statement:
                    block['fields'][field] = statement[field]
            return block
        return None

    def generate_laymen_code(self, visualBlocks):
        laymenCode = ""
        for block in visualBlocks:
            laymenCode += self.generate_statement(block)
        return laymenCode

    def generate_statement(self, block):
        blockType = block['type']
        if blockType in self.block_definitions:
            statement = self.block_definitions[blockType]['template']
            for field, value in block['fields'].items():
                statement = statement.replace('{' + field + '}', str(value))
            return statement + "\n"
        return ""
```