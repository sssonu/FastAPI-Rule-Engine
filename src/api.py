from flask import Flask, request, jsonify, render_template 
from werkzeug.urls import url_quote

from .rule_engine import create_rule, combine_rules, evaluate_rule
from .database import save_rule, get_rule
import json

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_rule', methods=['POST'])
def create_rule_route():
    rule_name = request.form['rule_name']
    rule_string = request.form['rule_string']
    
    try:
        rule = create_rule(rule_string)
        save_rule(rule_name, rule_string, rule)
        message = f"Rule '{rule_name}' created and saved successfully."
        return render_template('index.html', message=message)
    except Exception as e:
        error_message = f"Error creating rule: {str(e)}"
        return render_template('index.html', message=error_message, error=True)

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_route():
    rule_name = request.form['eval_rule_name']
    json_data = request.form['json_data']
    
    try:
        rule_string, ast_dict = get_rule(rule_name)
        if not ast_dict:
            raise ValueError(f"Rule '{rule_name}' not found")
        
        data = json.loads(json_data)
        result = evaluate_rule(ast_dict, data)
        
        return render_template('index.html', result=result)
    except Exception as e:
        error_message = f"Error evaluating rule: {str(e)}"
        return render_template('index.html', message=error_message, error=True)

@app.route('/combine_rules', methods=['POST'])
def combine_rules_route():
    rule_names = request.form['rule_names'].split(',')  # Split the input string into a list
    new_rule_name = request.form['new_rule_name']
    
    try:
        rules = []
        for name in rule_names:
            name = name.strip()  # Remove any leading/trailing whitespace
            rule_string, _ = get_rule(name)
            if rule_string is None:
                raise ValueError(f"Rule '{name}' not found")
            rules.append(rule_string)
        
        combined_rule = combine_rules(rules)
        save_rule(new_rule_name, str(combined_rule), create_rule(str(combined_rule)))
        message = f"Rules combined successfully into new rule '{new_rule_name}'."
        return render_template('index.html', message=message)
    except Exception as e:
        error_message = f"Error combining rules: {str(e)}"
        return render_template('index.html', message=error_message, error=True)