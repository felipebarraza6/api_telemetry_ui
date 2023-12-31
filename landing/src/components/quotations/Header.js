import React, { useContext } from 'react'
import { QuotationContext } from '../../containers/Quotation'
import { Steps } from 'antd'
import { ProfileOutlined, AppstoreOutlined, 
        LoadingOutlined, EyeOutlined, FileImageFilled } from '@ant-design/icons'

const Header = () => {
  const { state }  = useContext(QuotationContext)
  const steps = state.steps

  return(<>
    <Steps size='default' style={styles.container} 
       current = {steps.current} >
      {!steps.step01.hide && 
        <Steps.Step icon={<ProfileOutlined />}  title={window.innerWidth > 800 ? steps.step01.finish ? state.client.name_enterprise : steps.step01.title:''} />}
      {!steps.step02.hide && 
        <Steps.Step icon={<AppstoreOutlined />} title={window.innerWidth > 800? !state.wells.temporary_well.is_edit ? 
          steps.step02.title:
          <>Editando pozo: <b>{state.wells.temporary_well.general_data.name_well}</b></>:''} />}
      {!steps.step03.hide && 
        <Steps.Step icon={<LoadingOutlined />} status='process'  />}
      {!steps.step04.hide &&  
        <Steps.Step icon={state.wells.temporary_well.is_load_image ? <FileImageFilled /> :<EyeOutlined />} 
          title={state.wells.temporary_well.is_load_image ? state.wells.temporary_well.is_edit ? 'Editando tus imágenes':'Agrega tu imágenes':steps.step04.title} />}
    </Steps>
  </>)

}


const styles = {
  container: {
    padding: '20px',
    backgroundColor: 'white'
  }
}

export default Header
