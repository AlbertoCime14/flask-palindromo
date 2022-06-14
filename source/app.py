from flask import Flask, request, jsonify
import os
app = Flask(__name__)

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
            return "please, insert a string"
        else:
            palindrome =isPalindrome(strings_args)
            if palindrome:
                Dict = {"palindrome" : "True"}
                return Dict
            else:
                Dict = {"palindrome" : "False"}
                return Dict
    else:
        return "Error: No id field provided. Please specify a string"

    # Create an empty list for our results
    

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
   

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(strings_args)

if __name__=='__main__':
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)#port add


