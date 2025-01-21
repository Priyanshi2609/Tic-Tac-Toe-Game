const socket = io();

// Join the game
socket.emit('join_game');

// Track the game state
let board = ['', '', '', '', '', '', '', '', ''];
let currentPlayer = 'X';

function makeMove(index) {
    if (board[index] === '') {
        board[index] = currentPlayer;
        document.getElementsByClassName('cell')[index].innerText = currentPlayer;
        socket.emit('make_move', { move: index });
        currentPlayer = (currentPlayer === 'X') ? 'O' : 'X';
    }
}

function logout() {
    window.location.href = '/logout';
}

socket.on('game_started', (data) => {
    alert(`${data.player} has joined the game!`);
});

socket.on('game_start', () => {
    alert("Game has started!");
});

socket.on('update_board', (data) => {
    const { move, player } = data;
    board[move] = player === 'player1' ? 'X' : 'O';
    document.getElementsByClassName('cell')[move].innerText = player === 'player1' ? 'X' : 'O';
});

socket.on('game_full', () => {
    alert("The game is full. Please try again later.");
});

socket.on('player_left', (data) => {
    alert(`${data.player} has left the game.`);
});
