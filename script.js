
function validateForm() {
    let email = document.querySelector('input[type="email"]');
    let emails = document.querySelectorAll('input[type="email"]');

    let userID = document.querySelectorAll('input[type="text"]');

    // Check email
    if (emails[0].value !== emails[1].value) {
        alert("Email addresses do not match.");
        return false;
    }

    // Check User ID
    if (userID[1].value !== userID[2].value) {
        alert("Preferred User ID does not match.");
        return false;
    }

    // Check User ID length
    if (userID[1].value.length < 8 || userID[1].value.length > 20) {
        alert("User ID must be 8-20 characters.");
        return false;
    }

    // Check first character
    if (!/^[A-Za-z]/.test(userID[1].value)) {
        alert("The first character of the User ID must be a letter.");
        return false;
    }

    // Check allowed characters
    if (!/^[A-Za-z][A-Za-z0-9_]*$/.test(userID[1].value)) {
        alert("User ID can only contain letters, numbers, and underscore.");
        return false;
    }

    alert("Registration successful!");

    return true;
}