const initialState = {
    map: new Map()
};

const itemsReducer = (state = initialState, action) => {
    switch(action.type) {
        case 'items':
            const itemMap = new Map();
            for(let i = 0; i < action.json.data.length; i++) {
                itemMap.set(action.json.data[i].name, action.json.data[i].category);
            }
            return {
                map: itemMap,
            }
        default:
            return state
    }
}

export default itemsReducer;