<?php

/**
 * 
 */
class Unite_Helper {
	
	public static function get_typography_options(){

		$typography_options = array(
	        'sizes' => array( 
	        	'6px'  => '6px',
	        	'10px' => '10px',
	        	'12px' => '12px',
	        	'14px' => '14px',
	        	'15px' => '15px',
	        	'16px' => '16px',
	        	'18px' => '18px',
	        	'20px' => '20px',
	        	'24px' => '24px',
	        	'28px' => '28px',
	        	'32px' => '32px',
	        	'36px' => '36px',
	        	'42px' => '42px',
	        	'48px' => '48px'
	        ),
	        'faces' => array(
	                'arial'          => esc_html__( 'Arial', 'unite' ),
	                'verdana'        => esc_html__( 'Verdana, Geneva', 'unite' ),
	                'trebuchet'      => esc_html__( 'Trebuchet', 'unite' ),
	                'georgia'        => esc_html__( 'Georgia', 'unite' ),
	                'times'          => esc_html__( 'Times New Roman', 'unite' ),
	                'tahoma'         => esc_html__( 'Tahoma, Geneva', 'unite' ),
	                'Open Sans'      => esc_html__( 'Open Sans', 'unite' ),
	                'palatino'       => esc_html__( 'Palatino', 'unite' ),
	                'helvetica'      => esc_html__( 'Helvetica', 'unite' ),
	                'helvetica-neue' => esc_html__( 'Helvetica Neue, Helvetica, Arial, sans-serif', 'unite' )
	        ),
	        'styles' => array( 
	        	'normal' => esc_html__( 'Normal', 'unite' ),
	        	'bold'   => esc_html__( 'Bold', 'unite' )
	        ),
	        'color'  => true
		);

		return $typography_options;

	}

	public static function get_blog_layout(){

		$blog_layout = array(
			'1' => esc_html__( 'Display full content for each post', 'unite' ),
			'2' => esc_html__( 'Display excerpt for each post', 'unite' )
		);

		return $blog_layout;

	}

	public static function get_site_layout(){

		$site_layout = array(
			'side-pull-left'  => esc_html__( 'Right Sidebar', 'unite' ),
			'side-pull-right' => esc_html__( 'Left Sidebar', 'unite' ),
			'no-sidebar'      => esc_html__( 'No Sidebar', 'unite' ),
			'full-width'      => esc_html__( 'Full Width', 'unite' )
		);

		return $site_layout;

	}

}