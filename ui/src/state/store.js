import {useReducer, createContext} from "react";
import jobsReducer from "./jobsReducer";

export const initialState = {
    jobs: [],
    error: null,
    loading: false
};

const Store = ({children})=>{
    const [state, dispatch] = useReducer(jobsReducer, initialState);

    return (
        <Context.Provider value={[state, dispatch]}>
            {children}
        </Context.Provider>
    )

}

export const Context = createContext(initialState)

export default Store