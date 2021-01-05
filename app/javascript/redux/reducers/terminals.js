const initialState = {
    // an array containing 8 string arrays
    terminals: [[],[],[],[],[],[],[],[]]
};

const terminalsReducer = (state = initialState, action) => {
    switch(action.type) {
        case 'update':
            let updatedTerminals = state.terminals;
            updatedTerminals[action.index] = action.terminal;
            return {
                terminals: updatedTerminals,
            }
        case 'remove':
            let terminalRemoval = state.terminals;
            terminalRemoval.splice(action.index, 1);
            terminalRemoval.push([]);
            return {
                terminals: terminalRemoval,
            }
        default:
            return state
    }
}

export default terminalsReducer;