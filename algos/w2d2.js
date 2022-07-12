/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
    var newArray = str.split(" ");
    var newStr = '';
    for(var i = 0; i < newArray.length; i++){
        for( var j = newArray[i].length - 1; j >= 0; j--){
            newStr += newArray[i][j];
        }
        newStr += " ";
    }
    return newStr;
}

console.log(reverseWords(str1))