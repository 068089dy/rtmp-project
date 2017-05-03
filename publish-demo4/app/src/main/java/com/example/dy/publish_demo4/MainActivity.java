package com.example.dy.publish_demo4;

import android.app.AlertDialog;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import com.example.dy.publish_demo4.View.StateButton;
import com.github.faucamp.simplertmp.RtmpHandler;
import com.hanks.htextview.HTextView;
import com.hanks.htextview.HTextViewType;
import com.seu.magicfilter.utils.MagicFilterType;

import net.ossrs.yasea.SrsCameraView;
import net.ossrs.yasea.SrsEncodeHandler;
import net.ossrs.yasea.SrsPublisher;
import net.ossrs.yasea.SrsRecordHandler;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    public static final String RTMPURL_MESSAGE = "livertmppushsdk.demo.rtmpurl";
    private EditText Edit_rtmpurl;
    StateButton sbtn_start;
    HTextView hTextView;
    List<String> test_list = new ArrayList<String>();
    int text_i = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initview();

    }

    private void initview() {
        Edit_rtmpurl = (EditText) findViewById(R.id.Edit_rtmpurl);
        Edit_rtmpurl.setOnClickListener(this);

        test_list.add("这是你的rtmp推流地址");
        test_list.add("不要让别人知道");
        test_list.add("目前这个地址还很简单");
        test_list.add("后面我们会做处理");
        hTextView = (HTextView) findViewById(R.id.htext_);
        hTextView.setAnimateType(HTextViewType.ANVIL);
        hTextView.animateText(test_list.get(0)); // animate
        hTextView.setOnClickListener(this);


        sbtn_start = (StateButton) findViewById(R.id.sbtn_livestart);
        sbtn_start.setOnClickListener(this);
    }

    public void onClick(View v) {
        switch (v.getId()) {

            case R.id.sbtn_livestart:
                if (!Edit_rtmpurl.getText().toString().equals("")) {
                    Intent i = new Intent(MainActivity.this, liveActivity.class);
                    i.putExtra(MainActivity.RTMPURL_MESSAGE, Edit_rtmpurl.getText().toString());
                    startActivity(i);
                } else {
                    Toast.makeText(this, "推流地址不能为空", Toast.LENGTH_SHORT).show();
                }
                break;
            /*
            case R.id.htext_:

                if(test_list!=null) {
                    hTextView.setBottom(50);
                    hTextView.animateText(test_list.get(text_i));
                    if(text_i==(test_list.size()-1)){
                        text_i = 0;
                    }else {
                        text_i++;
                    }
                }
                break;
                */
            default:
                break;
        }

    }
}
