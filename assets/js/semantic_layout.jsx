import React, { Component } from 'react'
import {
  Button,
  Container,
  Header,
  Icon,
  Label,
  Segment,
  Visibility,
} from 'semantic-ui-react'
import Footer from './footer.jsx'
import FixedMenu from './FixedMenu.jsx'
import UpperMenu from './UpperMenu.jsx'

export default class HomepageLayout extends Component {
  constructor(props) {
    super(props)
    this.state = {}
    this.hideFixedMenu = this.hideFixedMenu.bind(this)
    this.showFixedMenu = this.showFixedMenu.bind(this)
  }

  hideFixedMenu() {
    this.setState({ visible: false })
  }

  showFixedMenu() {
    this.setState({ visible: true })
  }

  componentDidMount() {
    let now = new Date();
    let day = now.getDay()
    let hour = now.getHours()
    let minute = now.getMinutes()
    fetch(`http://127.0.0.1:8000/api/get/restaurant?day=${day}&hour=${hour}&minute=${minute}`)
      .then(res => res.json())
      .then(res => {

        let restaurants = res.map((res_obj) => {
          return (
            <Label key={res_obj.id}>
              <Icon name='food' />
              <Button content={res_obj.name} secondary />
            </Label>
          )
        })
        this.setState({ restaurant: restaurants })
      })

  }

  render() {
    const { visible } = this.state
    return (
      <div>
        {visible ? <FixedMenu active='首頁' /> : null}

        <Visibility
          onBottomPassed={this.showFixedMenu}
          onBottomVisible={this.hideFixedMenu}
          once={false}
        >
          <Segment
            inverted
            textAlign='center'
            style={{ minHeight: 700, padding: '1em 0em' }}
            vertical
          >
            <UpperMenu active='首頁' />

            <Container text>
              <Header
                as='h1'
                content='avancevl'
                inverted
                style={{ fontSize: '4em', fontWeight: 'normal', marginBottom: 0, marginTop: '3em' }}
              />
              <Header
                as='h1'
                content='餐廳資訊'
                inverted
                style={{ fontSize: '4em', fontWeight: 'normal' }}
              />
              <Button primary size='huge'>
                體驗訂餐
                <Icon name='right arrow' />
              </Button>
            </Container>
          </Segment>
        </Visibility>


        <Segment style={{ padding: '8em 0em' }} vertical>
          {this.state.restaurant}
        </Segment>

        <Footer />
      </div>
    )
  }
}
