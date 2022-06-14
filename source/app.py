from flask import Flask, request, jsonify
import os
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/', methods=['GET'])
def palindrome():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    def isPalindrome(s):
        return s == s[::-1]
    
    if 'string' in request.args:
        strings_args= request.args['string']
        if strings_args.isdigit() :
            return jsonify (
                    error = "the parameter is not a string"
                )
        else:
            palindrome =isPalindrome(strings_args)
            if palindrome:
                count = {}
                for i in strings_args:
                    if i in count: #check if it exists in dictionary
                        count[i] += 1
                    else:
                        count[i] = 1 #first occurrence of character
                return jsonify (
                    name = strings_args,
                    palindrome = palindrome,
                    sorted = count,
                    length = len(strings_args)
                )
            else:
                return jsonify (
                    name = strings_args,
                    palindrome = palindrome,
                )
    else:
     
        return jsonify (
                    error = "Error: No string field provided. Please specify a string"
                )

  

if __name__=='__main__':
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)#port add


