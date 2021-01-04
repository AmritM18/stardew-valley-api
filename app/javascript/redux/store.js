// Redux middleware provides a third-party extension point between
// dispatching an action and the moment it reaches the reducer.
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';

import rootReducer from './reducers';

export default function configureStore() {
    const store = createStore(
        rootReducer, 
        applyMiddleware(thunk)
    );
    return store;
}