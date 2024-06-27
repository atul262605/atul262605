includes
{

}

Variables
{
	DiagRequest Door.did_Write_1518 Write_DID_1518;
	
	DiagRequest Door.did_Read_1518 Read_DID_1518;
}

testcase DiagFuntion{
	
	if (0 != diagSetTarget("Door")
	{
		Write("Error in setting target");
	}
	testWaitForTimeout(1000);
	diagSetParameter(Write_DID_1518,"Byte_1",0x00);
	diagSendRequest(Write_DID_1518);
	testWaitForTimeout(1000);
   	diagSendRequest(Read_DID_1518);
}

void Main()
{
	DiagFuntion();
	
}

//------------------------------------------------------------------------
//Periodic send the message with capl

Variables
{
	msTimer Timer_VDC_A3;
	message VDC_A3 msg_VDC_A3;
}

On Start
{
	SetTimer(Timer_VDC_A3,100);
}

OnTimer Timer_VDC_A3
{
	output(msg_VDC_A3);
	SetTimer(Timer_VDC_A3,100);
}

on Key 'a'
{
	CancelTimer(Timer_VDC_A3);
}

//-------------------------------------------------------------------------------

DiagRequest Door.Serial_Number_Write W_Req;

DiagResponse Door.Serial_Number_Read R_Req;

// Create object for the "Serial Number Read" service
diagRequest Door.Serial_Number_Read myRequest; 


//send diag request
diagSendRequest(myRequest);


on key 'b'
{
	
 

DiagRequest Door.Serial_Number_Write W_Req;

byte Serial_Number[14]={0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,
                        0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF};

long res;

Write("Setting up raw parameter");

res=diagSetParameterRaw(W_req,"Serial_Number",Serial_Number,elcount(Serial_Number));

if res>=0
{
	res=diagSendRequest(W_req);
	
	if res>=0
	{
		write("Request has beend sent successfully");
	}
	
	else
	{
		write("Cound not send the request");
	}
}
}
//-----------------------------------------------------------------------------------------
// Receiving the response

on diagResponse Door.Serial_Number_Read
{
	//response event handler
	
	long res;
	byte Serial_Number[14];
	
	//reading Raw Parameters
	
	if( diagIsPositiveResponse)
	{	
		res=diagGetRawParameter(this,"Serial_Number" ,Serial_Number,elcount(Serial_Number));
	
		if res>=0
		{
			write("write the serial number in %02,%02,%02,Serial_Number[0],Serial_Number[1],Serial_Number[2]);
		}
		
		else
		{
			write("Not successful");
		}
		
	}
	
	else
	{
		diagGetResponseCode(this);
	}
	
}

//----------------------------------------------------------------------------------------------
//Reading the fault memory

on Key 'd'
{
	diagRequest Door.FaultMemory_ReadAllIdentifier Req;
	
	diagSetParameter(Req,"DTC status Mask",0x7F);
	
	diagSendRequest(Req);
}

on diagResponse Door.FaultMemory_ReadAllIdentifier
{
	long length;
	byte StatusByte;
	char test[200];
	byte bit;
	int i;
	dword  DTC;
	
	if (0 != diagIsPositiveResponse(this)
	{
		length = diagGetIterationCount(this,"ListofDTC);
		
		if(length >0)
		{
			StatusByte = diagGetRawParameter(this,"DtcAvailabilityMask");
			
			bit= diagGetRawParameter(this, DtcAvailabilityMask.TestFailed)
		}
	    for(i=0;i<=length;i++)
	    {
			DTC = diagGetComplexParameter(this,"ListOfDTC", i, "DTC");
			diagGetComplexParameter(this, "ListOfDTC", i, "DTC", text, elCount(text));
		
	    }
	
		
	}
}

//----------------------------------------------------------------------------------------------

variables
{
  //Golbal variables declaration
  msTimer timer_DIAG;
  byte checkByte0;  
  message 0x713 msg = { dlc=8}; //0x713 request msg Need help to fix when SID 2E is requested 
  byte check_byte0;
  message 0x71B sendmsg; //0x71B response msg
}

//First frame: 10 0A 2E F1 90 10 20 30

//Consecutive frame: 21 40 50 60 70 00 00 00

on key 'q'
{  
  msg.byte(0) = 0x10;
  msg.byte(1) = 0x0A
  msg.byte(2) = 0x2E;
  msg.byte(3) = 0xF1;
  msg.byte(4) = 0x90;
  msg.byte(5) = 0x10;
  msg.byte(6) = 0x20;
  msg.byte(7) = 0x30;
  output(msg);  
}

on message 0x713
{
  checkByte0 = this.byte(0) & 0x30;  
  if(checkByte0 == 0x30) //FC frame
  {
    msg.byte(0) = 0x21;
    msg.byte(1) = 0x40;    
    msg.byte(2) = 0x50;
    msg.byte(3) = 0x60;
    msg.byte(4) = 0x70;
    output(msg);
  }
}
//Request message from client to server 0x713 CAN ID 
on message 0x713
{
//  tester_DiagReqEds = this.tester_DiagReqEds;
//  write(" Request CAN msg 0x723 Received %x", tester_DiagReqEds);
  checkByte0 = this.byte(0) & 0x30;  
  if(checkByte0 == 0x30) //FC frame
  {
    msg.dlc = 8;
    msg.dword(0) = 0x30;
    msg.dword(4) = 0x00;    
    output(msg);
  }
}

//-----------------------------------------------------------------------

Variables
{
	msTimer Timer_VDC_A3;
	message VDC_A3 msg_VDC_A3;
	message 0x7C3 msg;
	byte Check_Byte;
}

On Start
{
	SetTimer(Timer_VDC_A3,100);
}

OnTimer Timer_VDC_A3
{
	output(msg_VDC_A3);
	SetTimer(Timer_VDC_A3,100);
}

on Key 'a'
{
	CancelTimer(Timer_VDC_A3);
}

//03 22 06 read request
on Key 'w'
{
	msg.byte(0) = 0x03;
	msg.byte(1) = 0x22;
	msg.byte(2) = 0x06;
	msg.byte(3) = 0x00;
	msg.byte(4) = 0x00;
	msg.byte(5) = 0x00;
	msg.byte(6) = 0x00;
	msg.byte(7) = 0x00;
	output(msg);
	
}

//Reponse from ECU
on message 0x7C9
{
	Check_Byte=this.byte(0)&0x30;
	
	if ( Check_Byte ==0x10)
	{
		msg.dword(0) = 0x30;
		msg.dword(1) = 0x00;
	}
	output(msg);
}

	