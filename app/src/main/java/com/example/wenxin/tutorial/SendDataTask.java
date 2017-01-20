package com.example.wenxin.tutorial;

import android.os.AsyncTask;
import android.util.Log;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;

/**
 * Created by javednissar on 2017-01-08.
 */
public class SendDataTask extends AsyncTask<Float, Void, Boolean>{
    private DatagramSocket socket;

    protected Boolean doInBackground(Float... rots){
        try{
            socket = new DatagramSocket(5959);
            String[] strings = new String[rots.length];
            for(int floatIndex = 0;floatIndex < rots.length;floatIndex++){
                strings[floatIndex] = rots[floatIndex].toString();
            }

            InetAddress targetAddress = InetAddress.getByName("192.168.137.1");
            StringBuilder dataConstructor = new StringBuilder();
            for(int stringIndex = 0;stringIndex < strings.length;stringIndex++){
                dataConstructor.append(strings[stringIndex]);
                dataConstructor.append('!');
            }
            byte[] dataToSendAsBytes = dataConstructor.toString().getBytes();
            DatagramPacket packet =  new DatagramPacket(dataToSendAsBytes,
                    dataToSendAsBytes.length,
                    targetAddress,
                    5959);
            socket.send(packet);
            Log.d("Yay","Message sent");
            return true;
        }catch(UnknownHostException e) {
            Log.e("WTF", e.getMessage());
            return false;
        }catch(IOException e){
            Log.e("WTF", e.getMessage());
            return false;
        }
    }

    protected void onPostExecute(Boolean result){
        if(result){
            socket.close();
        }
    }
}
