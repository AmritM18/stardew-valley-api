const initialState = {
    map: new Map(),
    craftCategories: []
};

const itemsReducer = (state = initialState, action) => {
    switch(action.type) {
        case 'items':
            const itemMap = new Map();
            let categories = [];
            for(let i = 0; i < action.json.data.length; i++) {
                if(action.json.data[i].category === "crafting") {
                    categories.push(action.json.data[i].name);
                }
                else {
                    itemMap.set(action.json.data[i].name.toLowerCase(), action.json.data[i].category);
                }
            }
            return {
                map: itemMap,
                craftCategories: categories
            }
        default:
            return state
    }
}

export default itemsReducer;