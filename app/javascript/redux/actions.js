export function getItems() {
    return (dispatch) => {
        $.getJSON('/item')
          .then(response => dispatch(getThingsSuccess('items', response)))
          .catch(error => console.log(error));
      };
};

export function getThingsSuccess(type, json) {
    return {
        type: type, json
    };
};