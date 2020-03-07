import React from 'react'
import {Table, Menu, Label, Input, Button, Header, Image, Modal, Icon } from 'semantic-ui-react'
var Markdown = require('react-remarkable');

const ResultTable = (props) => {
  return (
	<Table celled>
	  <Table.Header>
	  	<Table.Row>
	  	  <Table.HeaderCell>查詢單子:{props.result.key}</Table.HeaderCell>
	  	  <Table.HeaderCell>similarity:{props.result.similarity}</Table.HeaderCell>
	  	</Table.Row>
		<Table.Row>
		  <Table.HeaderCell>單字</Table.HeaderCell>
		  <Table.HeaderCell>分數</Table.HeaderCell>
		</Table.Row>
	  </Table.Header>

	  <Table.Body>
		{
			props.result.value.map((item, idx) => (
				<Table.Row key={idx}>
				  <Table.Cell>{item[0]}</Table.Cell>
				  <Table.Cell>{item[1]}</Table.Cell>
				</Table.Row>
				))
		}
	  </Table.Body>
	</Table>
  )
}

const ResultTableOnlyAns = (props) => {
  return (
	<Table celled>
	  <Table.Header>
		<Table.Row>
		  <Table.HeaderCell>結果</Table.HeaderCell>
		</Table.Row>
	  </Table.Header>

	  <Table.Body>
	  	<Table.Row>
	  	  <Table.Cell>{props.result.result}</Table.Cell>
	  	</Table.Row>
	  </Table.Body>
	</Table>
  )
}

class InputExampleInput extends React.Component {
	constructor(props) {
	  super(props);
	  this.state = {
		result:{"key":"", "value":[], "similarity":""}
	  }
	this.handleKeypress = this.handleKeypress.bind(this)
	}

	handleKeypress(event){
	  if(event.key == 'Enter'){
			$.getJSON( this.props.url + event.target.value, (result) => {
				this.setState({'result': result})
			})
	  }
	}

	render() {
		return(
			<div>
				<Input placeholder='Search...' onKeyUp={this.handleKeypress}/>
				{this.props.oneColumn ? (
					<ResultTableOnlyAns result={this.state.result}/>
				) : (
					<ResultTable result={this.state.result}/>
				)}
			</div>
		)
	}
}

const ApiDemoModal = (props) => (
	<div>
	  <Header as='h3' style={{ fontSize: '2em' }}>{props.name}</Header>
	  <p style={{ fontSize: '1.33em' }}>
		{props.intro}
	  </p>
	  <Modal trigger={<Button>試用API</Button>}>
		<Modal.Header>{props.name}</Modal.Header>
		<Modal.Content image>
		  <Image wrapped size='medium' src={props.picture} />
		  <Modal.Description>
			<Header>使用說明</Header>
			<Markdown source={props.descript} />            
			<InputExampleInput url={props.url} oneColumn={props.oneColumn}/>
		  </Modal.Description>
		</Modal.Content>
	  </Modal>
	</div>
)

export default ApiDemoModal