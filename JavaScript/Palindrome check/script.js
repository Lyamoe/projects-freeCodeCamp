function checkPali(){
    console.log("Click worked")
    const input = document.getElementById('text-input').value;
    const lc = input.toLowerCase();
    const word = lc.replace(/[^a-zA-Z0-9]/g, '');
    const result = document.getElementById('result');
    const initial = document.getElementById('initial');
    const final = document.getElementById('final');
    let backward = "";

    if (word == "") {
        console.warn("User didn't insert a word");
        window.alert("Please input a value")
    } else {
        if (word.length){
            for (let wordLength = word.length; wordLength > 0; wordLength--){
                backward += word.charAt(wordLength-1);
            }
        }

        if (word == backward){
            result.innerText = input + " is a palindrome";
        } else {
            result.innerText = input + " is not a palindrome";
        }

        initial.innerText = "''" + word;
        final.innerText = backward + "''";
    }
}