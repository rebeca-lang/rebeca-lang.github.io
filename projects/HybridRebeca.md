---
layout: page
title: Hybrid Rebeca
permalink: /allprojects/HybridRebeca

---

#### Description

Hybrid Rebeca, is an extension of actor-based language Rebeca, to support modeling of cyber-physical systems. In this extension, physical actors are introduced as new computational entities to encapsulate the physical behaviors. To support various means of communication among the entities, network is explicitly modeled as a separate entity from actors. We derive hybrid automata as the basis for analysis of Hybrid Rebeca models.
In this version, CAN network is defined as network model for communications of the actors. Actors can communicate with each other either through the CAN network or directly by wire.

<script type="text/javscript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js" ></script>

<script type="text/javascript">
function showit() {
  var x = document.getElementById("myDIV");
  if ($("#myDIV").is(":visible")) {
      $("#myDIV").hide(1000);
  } else {
      $("#myDIV").show(1000);
  }
}
</script>

#### Tools
We developed a tool which implements the core rules of Hybrid Rebeca. No parser is implemented in the current version of the tool, so the textual models can’t directly be used with the tool and the models must be manually defined by code.
The output of our tool for a model, is a hybrid automaton in the format of SpaceEx. SpaceEx is a framework for verification hybrid systems. Verification of the model can be done by giving the output file to the SpaceEx tool.

#### Case Studies
* Water Tank: <a class="link link_show" onclick="showit()">show</a> 
<a class="link link_download" href="/assets/projects/HybridRebeca/case-studies/WaterTank.rebeca">download</a>
<div id="myDIV">
{% highlight java linenos %}
physicalclass Tank {
    knownrebecs{}
    statevars{
        real amount; 
        float inFlowCap, outFlowCap, inRate, outRate;
    }

    msgsrv initial(foat amount_, float inFlowCap_, float outFlowCap_){
        amount = amount_;
        inFlowCap = inFlowCap_;
        outFlowCap = outFlowCap_;
        SetMode(NotEmpty);
    }
    
    msgsrv OpenOutput(){
        outRate = outFlowCap;
    }
    
    msgsrv CloseOutput(){
        outRate = 0;
    }
    
    msgsrv OpenInput(){
        inRate = inFlowCap;
    }
    
    msgsrv CloseInput(){
        inRate = 0;
    }
    
    mode NotEmpty{
        inv(amount >= 0) {
            amount' = inRate - outRate;
        }
        guard(amount == 0) {
            setmode(Empty);
        }
    }
    
    mode Empty{
        inv(amount==0){
            amount' = inRate;
        }
        guard(amount>0)
            setmode(NotEmpty);
    }
}

physicalclass Sensor {
    knownrebecs{ 
        Controller controller;
        Tank tank;
    }
    
    statevars{
        real timer;
    }
    
    msgsrv initial(){
        setmode(Active);
    }
    
    mode Active{
        inv(timer<=0.05){
            timer' = 1;
        }
        guard(timer==0.05){
            timer = 0;
            setmode(Active);
            controller.setTankAmount(tank.amount);
        }
    }
}

softwareclass Controller {
    knownrebecs { 
        Tank tank;
    }
    
    statevars {
        float tankAmount;
    }
    
    msgsrv initial(){
        tank.OpenOutput();
    }
    
    msgsrv setTankAmount(float amount){
        tankAmount = amount;
    }
    
    msgsrv control() {
        if(tankAmount <= 20)
            tank.OpenInput();
        if(tankAmount >= 30)
            tank.CloseInput();
        
    }
}

physicalclass Clock {
    knownrebecs{ 
        Controller controller;
    }
    
    statevars{
        real timer;
    }
    
    msgsrv initial(){
        setmode(Active);
    }
    
    mode Active{
        inv(timer<=0.1){
            timer' = 1;
        }
        guard(timer==0.1){
            timer = 0;
            setmode(Active);
            controller.control();
        }
    }
}

main {
    Tank tank ():(25,3,2);    
    Sensor sensor(@CAN controller,@Wire tank):();
    Controller controller (@CAN tank):();
    Clock clock(@Wire controller):();

    CAN{
        priorities{
            controller tank.CloseInput              1
            controllertank.CloseOutput              2
            controllertank.OpenInput                3
            controller tank.OpenOutput              4
            sensor controller.setTankAmount         5
        }
        delays{
            controller tank.CloseInput -> 0.01
            controller tank.CloseOutput -> 0.01
            controller tank.OpenInput -> 0.01
            controller tank.OpenOutput -> 0.01
            sensor controller.setTankAmount -> 0.01
            
        }
    }
}
{% endhighlight %}
</div>


#### Project Members
* **<u>Marjan Sirjani (Principal Investigator)</u>**
* **<u>Fatemeh Ghassemi (Principal Investigator)</u>**
* Iman Jahandideh

#### Related Publications
* Iman Jahandideh, Fatemeh Ghassemi, Marjan Sirjani: Hybrid Rebeca: Modeling and Analyzing of Cyber-Physical Systems, CyPhy, 2018
\\
<a class="link link_pdf" href="/assets/papers/2018/Hybrid-Rebeca-Modeling-and-Analyzing-of-Cyber-Physical-System.pdf">PDF</a>
