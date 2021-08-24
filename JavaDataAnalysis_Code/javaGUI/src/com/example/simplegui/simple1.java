package com.example.simplegui;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.BoxLayout;
import javax.swing.JLabel;
import java.awt.FlowLayout;
import javax.swing.JComboBox;
import java.awt.Font;
import java.awt.Color;
import java.awt.SystemColor;
import javax.swing.JTextField;
import javax.swing.JPasswordField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JProgressBar;

public class simple1 extends JFrame {

	private JPanel contentPane;
	private JTextField txtusername;
	private JPasswordField pwpield;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					simple1 frame = new simple1();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public simple1() {
		setTitle("learn java");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 558, 431);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JComboBox comboBox = new JComboBox();
		comboBox.setToolTipText("1");
		comboBox.setMaximumRowCount(5);
		comboBox.setFont(new Font("궁서", Font.BOLD, 12));
		comboBox.setBounds(248, 37, 199, 35);
		contentPane.add(comboBox);
		
		JLabel lblNewLabel = new JLabel("simple java gui");
		lblNewLabel.setForeground(SystemColor.textText);
		lblNewLabel.setBackground(SystemColor.controlDkShadow);
		lblNewLabel.setFont(new Font("맑은 고딕", Font.BOLD, 24));
		lblNewLabel.setBounds(33, 30, 193, 35);
		contentPane.add(lblNewLabel);
		
		JLabel lblNewLabel_1 = new JLabel("user name");
		lblNewLabel_1.setFont(new Font("굴림", Font.PLAIN, 16));
		lblNewLabel_1.setBounds(34, 119, 85, 35);
		contentPane.add(lblNewLabel_1);
		
		JLabel lblNewLabel_2 = new JLabel("pw");
		lblNewLabel_2.setFont(new Font("굴림", Font.PLAIN, 16));
		lblNewLabel_2.setBounds(59, 147, 26, 35);
		contentPane.add(lblNewLabel_2);
		
		txtusername = new JTextField();
		txtusername.setBounds(122, 119, 130, 30);
		contentPane.add(txtusername);
		txtusername.setColumns(10);
		
		pwpield = new JPasswordField();
		pwpield.setBounds(122, 151, 130, 30);
		contentPane.add(pwpield);
		
		JButton login = new JButton("login");
		login.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		login.setBounds(122, 219, 118, 30);
		contentPane.add(login);
		
		JButton exit = new JButton("exit");
		exit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				System.exit(0);
			}
		});
		exit.setBounds(265, 219, 118, 30);
		contentPane.add(exit);
		
		JProgressBar progressBar = new JProgressBar();
		progressBar.setValue(50);
		progressBar.setBounds(106, 191, 146, 14);
		contentPane.add(progressBar);
	}
}
