import re
from .data_structure import Node, dict_to_node

def create_rule(rule_string):
    def parse_expression(tokens):
        if len(tokens) == 1:
            return Node("operand", tokens[0])
        
        for op in ["AND", "OR"]:
            if op in tokens:
                idx = tokens.index(op)
                left = parse_expression(tokens[:idx])
                right = parse_expression(tokens[idx+1:])
                return Node("operator", op, left, right)
        
        for op in [">", "<", "=", ">=", "<="]:
            if op in tokens:
                idx = tokens.index(op)
                left = Node("operand", tokens[idx-1])
                right = Node("operand", tokens[idx+1])
                return Node("operator", op, left, right)
    
    tokens = re.findall(r'\(|\)|[\w\']+|>=|<=|>|<|=', rule_string)
    return parse_expression(tokens)

def combine_rules(rules):
    if not rules:
        return None
    if len(rules) == 1:
        return create_rule(rules[0])
    
    combined = Node("operator", "AND")
    combined.left = create_rule(rules[0])
    combined.right = combine_rules(rules[1:])
    return combined

def evaluate_rule(ast_dict, data):
    def evaluate_node(node):
        if node['type'] == 'operand':
            return data.get(node['value'], node['value'])
        
        left = evaluate_node(node['left'])
        right = evaluate_node(node['right'])
        
        if node['value'] == 'AND':
            return left and right
        elif node['value'] == 'OR':
            return left or right
        elif node['value'] in ['>', '<', '=', '>=', '<=']:
            return eval(f"{left} {node['value']} {right}")
    
    return evaluate_node(ast_dict)

def combine_rules(rules):
    if not rules:
        return None
    if len(rules) == 1:
        return rules[0]
    
    return f"({') AND ('.join(rules)})"












