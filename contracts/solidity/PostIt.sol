// contracts/PostIt.sol
// SPDX-License-Identifier: None

pragma solidity ^0.7.0;

contract PostIt{
    string public message;

    event NewMessage(string _message);

    constructor(string memory _message) {
        message = _message;
    }

    function setMessage(string memory _message) public {
        message = _message;
        emit NewMessage(_message);
    }

    function getMessage() public view returns (string memory) {
        return message;
    }
}