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
function showit(divID) {
  if ($(divID).is(":visible")) {
      $(divID).hide(1000);
  } else {
      $(divID).show(1000);
  }
}
</script>

#### Tools
We developed a tool which implements the core rules of Hybrid Rebeca. No parser is implemented in the current version of the tool, so the Rebeca models can’t directly be used with the tool.
Rebeca models are mapped manually to an intermediate code, and the intermediate code is fed to our tool.
The output of our tool is a hybrid automaton equivalent to the Hybrid Rebeca model in the format of SpaceEx. SpaceEx is a framework for verificationhybrid systems. Verification of the model can be done by giving the output file to the SpaceEx tool.

#### Case Studies
* Water Tank: <a class="link link_show" onclick="showit('#WaterTank')">show</a> 
<a class="link link_download" href="/assets/projects/HybridRebeca/case-studies/WaterTank.rebeca">download</a>
<div id="WaterTank" style="display: none;">
{% highlight java linenos %}
physicalclass Tank {
    knownrebecs{}
    
    statevars{
        real amount; 
        float inFlowCap, outFlowCap, inRate, outRate;
    }
    
    msgsrv initial(foat amount_, float inFlowCap_, float outFlowCap_) {
        amount = amount_;
        inFlowCap = inFlowCap_;
        outFlowCap = outFlowCap_;
        setMode(NotEmpty);
    }
    
    msgsrv OpenOutput() {
        outRate = outFlowCap;
    }
    
    msgsrv CloseOutput(){
        outRate = 0;
    }
    
    msgsrv OpenInput() {
        inRate = inFlowCap;
    }
    
    msgsrv CloseInput() {
        inRate = 0;
    }
    
    mode NotEmpty {
        inv(amount >= 0) {
            amount' = inRate - outRate;
        }
        guard(amount == 0) {
            setmode(Empty);
        }
    }
    
    mode Empty {
        inv(amount==0) {
            amount' = inRate;
        }
        guard(amount>0)
            setmode(NotEmpty);
    }
}

physicalclass Sensor {
    knownrebecs { 
        Controller controller;
        Tank tank;
    }
    
    statevars {
        real timer;
    }
    
    msgsrv initial() {
        setmode(Active);
    }
    
    mode Active {
        inv(timer<=0.05) {
            timer' = 1;
        }
        guard(timer==0.05) {
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
    
    msgsrv initial() {
        tank.OpenOutput();
    }
    
    msgsrv setTankAmount(float amount) {
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
    knownrebecs { 
        Controller controller;
    }
    
    statevars {
        real timer;
    }
    
    msgsrv initial() {
        setmode(Active);
    }
    
    mode Active {
        inv(timer<=0.1) {
            timer' = 1;
        }
        guard(timer==0.1) {
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

    CAN {
        priorities {
            controller     tank.CloseInput                   1
            controller     tank.CloseOutput                  2
            controller     tank.OpenInput                    3
            controller     tank.OpenOutput                   4
            sensor         controller.setTankAmount          5
        }
        delays {
            controller     tank.CloseInput                   0.01
            controller     tank.CloseOutput                  0.01
            controller     tank.OpenInput                    0.01
            controller     tank.OpenOutput                   0.01
            sensor         controller.setTankAmount          0.01
            
        }
    }
}
{% endhighlight %}
</div>
* Vending Machine: <a class="link link_show" onclick="showit('#VendingMachine')">show</a> 
<a class="link link_download" href="/assets/projects/HybridRebeca/case-studies/VendingMachine.rebeca">download</a>
<div id="VendingMachine" style="display: none;">
{% highlight java linenos %}
physicalclass Heater {
    knownrebecs {Controller controller;}
    statevars {real drinkTemp;}
    
    msgsrv initial() {
    }
    
    mode On {
        inv (drinkTemp <= 90) {
            drinkTemp' = (120 - drinkTemp)/20;
        }
        guard(drinkTemp == 90) {
            controller.drinkHeated();
            setmode(Off);
        }
    }
    
    mode Off {
        inv (drinkTemp >= 25) {
            drinkTemp' = drinkTemp - 10;
        }
        guard(drinkTemp == 25) {
            setmode(none);
        }
    }
}

softwareclass Controller {
    knownrebecs{UserInterface userIn; Heater heater;}
    statevars {int nCoffee;}
    
    msgsrv initial(int nCoffee_) {
        nCoffee = nCoffee_;
    }
    
    msgsrv prepareCoffee() {
        if(nCoffee<=0)
            userIn.alertNoCoffee();
        else
            heater.setMode(On);     
    }
    
    msgsrv drinkHeated() {
        nCoffee = nCoffee -1;
        userIn.deliverCoffee();
    }
}

softwareclass UserInterface {
    knownrebecs{Controller controller}
    
    msgsrv initial(){
        self.requestCoffee();
    }
    
    msgsrv requestCoffee() {
        controller.prepareCoffee();
    }
    
    msgsrv deliverCoffee() {
        delay(1);
        self.requestCoffee();
    }
        
    msgsrv alertNoCoffee() {
    }
}

main {
    Heater heater(@Wire controller):();
    Controller controller(@Wire userIn,@Wire heater):(10);
    UserInterface userIn(@Wire controller):();
    
    CAN {
        priorities {
        }
        delays {
        }
    }
}
{% endhighlight %}
</div>
* Brake by Wire: <a class="link link_show" onclick="showit('#BrakeByWire')">show</a> 
<a class="link link_download" href="/assets/projects/HybridRebeca/case-studies/BrakeByWire.zip">download</a>
<div id="BrakeByWire" style="display: none;">
{% highlight java linenos %}
physicalclass Wheel {
    knownrebecs {WCtlr ctlr;}
    statevars {float trq; real spd; real t;}
    msgsrv initial(float spd_) {
        spd = spd_;
        setmode(Rolling);
    }
    msgsrv setTrq(float trq_) {
        trq = trq_;    
    }
    mode Rolling {
        inv(t <= 0.05) {
            t' = 1;
            spd' = -0.1-trq;
        }
        guard(t == 0.05) {
            t = 0;
            ctlr.setWspd(spd);
            if(spd > 0)
                setmode(Rolling);
        }
    }
}
    
softwareclass WCtlr {
    knownrebecs {Wheel w; BrakeCtlr bctlr;}
    statevars {int id; float wspd; float slprt;}
    msgsrv initial(int id_) {
        id = id_;
    }
    msgsrv setWspd(float wspd_) {
        wspd = wspd_;
        bctlr.setWspd(id,wspd);
    }
    msgsrv applyTrq(float reqTrq, float vspd) {
        if(vspd == 0)
            slprt = 0;
        else
            slprt = (vspd - wspd * WRAD)/vspd;
        if(slprt > 0.2)
            wheel.setTrq(0);
        else
            wheel.setTrq(reqTrq);
    }
}

physicalclass Brake {
    knownrebecs {BrakeCtlr bctlr;}
    statevars {real bprcnt; real t; float mxprcnt; float r}
    msgsrv initial(float bprcnt_, float mxprcnt_) {
        bprcnt = bprcnt_;
        mxprcnt = mxprcnt_;
        r = 1;
        setmode(Braking);
    }
    mode Braking {
        inv(t <= 0.05) {
            t' = 1;
            bprcnt' = r;
        }
        guard(t == 0.05) {
            t = 0;
            bctrl.setBprcnt(bprcnt);
            if(bprcnt>=mxprcnt)
                r = 0;
            setmode(Braking);
        }
    }
}

softwareclass BrakeCtlr {
    knownrebecs {WCtlr wctlrR;WCtlr wctlrL;}
    statevars {float wspdR;float wspdL;float bprcnt;float gtrq;float espd;}
    msgsrv control() {
        espd = (wspdR + wspdL)/2;
        gtrq = bprcnt;
        wctlrR.applyTrq(gtrq, espd);
        wctlrL.applyTrq(gtrq, espd);
    }
    // Setters for wspdR, wspdL and bprcnt
    ...
}

physicalclass Clock {
    knownrebecs {BrakeCtlr bctlr;}
    statevars {real t;}
    msgsrv initial() {
        setmode(Running)
    }
    mode Running() {
        inv(t <= 0.05) {
            t' = 1;
        }
        guard(t == 0.05) {
            t = 0;
            bctlr.control();
            setmode(Running);
        }
    }
}

main {
    Wheel wR (@Wire wctlrR):(1);
    Wheel wL (@Wire wctlrL):(1);
    WCtlr wctlrR (@Wire wR, @CAN bctlr):(0);
    WCtlr wctlrL (@Wire wL, @CAN bctlr):(1);
    BrakeCtlr bctlr (@CAN wctlrR, @CAN wctlrL):();
    Brake brake(@Wire bctlr):(60,65);
    Clock clock(@Wire bctlr):();
    
    CAN {
        priorities {
            bctlr     wctlrR.applyTrq      1;
            bctlr     wctlrL.applyTrq      2;
            wctlrR    bctlr.setWspd        3;
            wctlrL    bctlr.setWspd        4;
        }
        delays {
            bctlr     wctlrR.applyTrq      0.01;
            bctlr     wctlrL.applyTrq      0.01;
            wctlrR    bctlr.setWspd        0.01;
            wctlrL    bctlr.setWspd        0.01;
        }
    }
}
{% endhighlight %}
</div>
* Complex Heater: <a class="link link_show" onclick="showit('#ComplexHeater')">show</a> 
<a class="link link_download" href="/assets/projects/HybridRebeca/case-studies/ComplexHeater.zip">download</a>
<div id="ComplexHeater" style="display: none;">
{% highlight java linenos %}
physicalclass Heater {
    knownrebecs { 
        Controller controller;
    }
    statevars {
        real temp, timer;
    }
    
    msgsrv initial(float temp_) {
        temp = temp_;
        setmode(On);
    }
    
    mode On {
        inv(timer<=0.05) {
            timer' = 1;
            temp' = 4-0.1*temp;
        }
        guard(timer==0.05) {
            timer = 0;
            controller.control(temp);
        }
    }
    
    mode Off {
        inv(timer<=0.05) {
            timer' = 1;
            temp' = -0.1*temp;
        }
        guard(timer==0.05) {
            timer = 0;
            controller.control(temp);
        }
    }
}

softwareclass Controller {
    knownrebecs { 
        Heater heater;
    }
    statevars {}
    
    msgsrv initial() {
    }
    
    msgsrv control(float temp) {
        if(temp >= 22)
            heater.SetMode(Off);
        if(temp <= 18)
            heater.SetMode(On);
    }
}

main {
    Heater heater (@CAN controller):(20);    
    Controller controller (@CAN heater):();
    
    CAN {
        priorities {
            heater controller.control 0
            controlller heater.SetMode 1
        }
        delays {
            heater controller.control  0.01
            controller heater.SetMode  0.01
        }
    }
}
{% endhighlight %}
</div>

#### Project Members
* **<u>Fatemeh Ghassemi (Principal Investigator)</u>**
* Marjan Sirjani
* Iman Jahandideh

#### Related Publications
* Iman Jahandideh, Fatemeh Ghassemi, Marjan Sirjani: Hybrid Rebeca: Modeling and Analyzing of Cyber-Physical Systems, CyPhy, 2018
\\
<a class="link link_pdf" href="/assets/papers/2018/Hybrid-Rebeca-Modeling-and-Analyzing-of-Cyber-Physical-System.pdf">PDF</a>
