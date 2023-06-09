import * as actionTypes from '../actions/actionTypes';
import { updateObject } from '../utility';

// we need to define our initial state, of the entire application,
// like loading, authentication, token, etc.

const initialState = {
    token: null,
    error: null,
    loading: false,
    thisurl: null,
    course: null,
}

// authStart takes the action so that error is null and loading is true
// The spinner will start spinning once authStart is dispatched.
// When authSuccess is dispatched, we say the loading is false and
// and spinner will disappear.
const authStart = (state, action) => {
    return updateObject(state, {
        error: null,
        loading: true
    });
}

const authSuccess = (state, action) => {
    return updateObject(state, {
        token: action.token,
        course: action.course,
        error: null,
        loading: false
    });
}

const authFail = (state, action) => {
    return updateObject(state, {
        error: action.error,
        loading: false
    });
}

const authLogout = (state, action) => {
    return updateObject(state, {
        token: null,
        course: null,
    })
}

const setUrl = (state, action) => {
    return updateObject(state, {
        thisurl: action.thisurl,
    });
}




const reducer = (state = initialState, action) => {
    switch (action.type) {
        case actionTypes.AUTH_START: return authStart(state, action);
        case actionTypes.AUTH_SUCCESS: return authSuccess(state, action);
        case actionTypes.AUTH_FAIL: return authFail(state, action);
        case actionTypes.AUTH_LOGOUT: return authLogout(state, action);
        case actionTypes.SET_URL: return setUrl(state, action);
        default:
            return state;
    }
}

export default reducer;