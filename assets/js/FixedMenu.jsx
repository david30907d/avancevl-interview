var React = require('react')
import {
  Button,
  Container,
  Menu,
} from 'semantic-ui-react'

const FixedMenu = (props) => {
  let activeTable = {
    '首頁':'item',
  }
  activeTable[props.active] = 'item active'
  return(
  <Menu fixed='top' size='large'>
    <Container>
      <a className={activeTable['首頁']} href='/' >首頁</a>
      <Menu.Menu position='right'>
        <Menu.Item className='item'>
          <Button as='a'>Log in</Button>
        </Menu.Item>
        <Menu.Item>
          <Button as='a' primary>Sign Up</Button>
        </Menu.Item>
      </Menu.Menu>
    </Container>
  </Menu>)
}

export default FixedMenu;