import sqlite3
import json
from .data_structure import node_to_dict, dict_to_node

def init_db():
    conn = sqlite3.connect('rules.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS rules
                 (id INTEGER PRIMARY KEY, name TEXT UNIQUE, rule_string TEXT, ast_json TEXT)''')
    conn.commit()
    conn.close()

def save_rule(name, rule_string, ast):
    conn = sqlite3.connect('rules.db')
    c = conn.cursor()
    ast_json = json.dumps(node_to_dict(ast))
    c.execute("INSERT OR REPLACE INTO rules (name, rule_string, ast_json) VALUES (?, ?, ?)",
              (name, rule_string, ast_json))
    conn.commit()
    conn.close()

def get_rule(name):
    conn = sqlite3.connect('rules.db')
    c = conn.cursor()
    c.execute("SELECT rule_string, ast_json FROM rules WHERE name = ?", (name,))
    result = c.fetchone()
    conn.close()
    if result:
        rule_string, ast_json = result
        return rule_string, json.loads(ast_json)
    return None, None
