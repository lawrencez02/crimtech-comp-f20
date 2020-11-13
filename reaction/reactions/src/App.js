import logo from './logo.svg';
import './App.css';
import React from 'react';

class Panel extends React.Component {
  constructor(props) {
    super(props);
    this.state = {start_time: 0, ran_once: false, counting: false, true_duration: 0, reaction_time: 0, color: 'green'};
    this.process_click = this.process_click.bind(this);
  }
  handle_color = (c) => {
    this.setState({color: c});
    // console.log(window.performance.now());
  }
  start_count() {
    // console.log(window.performance.now());
    this.setState({start_time: Date.now()});
    var randomtime = Math.random() * 5 + 2;
    this.setState({true_duration: randomtime});
    this.setState({counting: true});
    this.setState({color: 'darkred'});
    setTimeout(this.handle_color, randomtime * 1000, 'green');
    // console.log(window.performance.now());
  }
  end_count() {
    // console.log(window.performance.now());
    var timepassed = Date.now() - this.state.start_time
    if (this.state.true_duration * 1000 <= timepassed)
    {
      this.setState({reaction_time: timepassed - (this.state.true_duration * 1000)});
      this.setState({ran_once: true});
      this.setState({counting: false});
    }
  }
  process_click() {
    if (this.state.counting) 
    {
      this.end_count();
    } 
    else 
    {
      this.start_count();
    }
  }
  render() {
    let msg = "Hello World!";
    if (this.state.counting && this.state.color === 'darkred')
    {
      msg = "Wait for Green";
    }
    else if (this.state.counting && this.state.color === 'green')
    {
      msg = "Click!";
    }
    else if (this.state.ran_once)
    {
      msg = "Your reaction time is " + this.state.reaction_time.toFixed(2) + " ms";
    }
    else
    {
      msg = "Click me to begin!"
    }
    return (
      <div className = "PanelContainer" onMouseDown = {this.process_click} style={ { background: this.state.color} }>
        <div className = "Panel">{msg}</div>
      </div>
    );
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1 className =  "Header">How Fast is your Reaction Time?</h1>
        <Panel />
        <p>Click as soon as the red box turns green. Click anywhere in the box to start.</p>
      </header>
    </div>
  );
}

export default App;
