import React, { useEffect } from 'react'


const LiftingRedirect = () => {
    
    useEffect(()=> {
        window.location.assign('http://smarthydroapp.cl/liftings/external')
    }, [])

    return(<></>)
    
}


export default LiftingRedirect