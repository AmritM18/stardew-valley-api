export function getItems() {
    return (dispatch) => {
        $.getJSON('/item')
          .then(response => dispatch(getItemsSuccess('items', response)))
          .catch(error => console.log(error));
      };
};

export function getItemsSuccess(type, json) {
    return {
        type, json
    };
};

export function updateResults(index, terminal) {
    return {
        type: 'update', index, terminal
    }
}

export function removeResults(index) {
    return {
        type: 'remove', index
    }
}