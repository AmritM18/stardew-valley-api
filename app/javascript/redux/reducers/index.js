import itemsReducer from './items';
import terminalsReducer from './terminals';
import {combineReducers} from 'redux';

const rootReducer = combineReducers({
    itemsReducer, 
    terminalsReducer
});

export default rootReducer;